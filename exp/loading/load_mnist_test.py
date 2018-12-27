"""Test MNIST data loader."""

from bpexts.utils import torch_allclose
from .load_mnist import MNISTLoader


def test_deterministic_loading():
    """Test deterministc loading of samples."""
    mnist1 = MNISTLoader(10, 0)
    train1 = mnist1.train_loader()
    train1_samples, train1_labels = next(iter(train1))

    mnist2 = MNISTLoader(10, 0)
    train2 = mnist2.train_loader()
    train2_samples, train2_labels = next(iter(train2))

    assert torch_allclose(train1_samples, train2_samples)
    assert torch_allclose(train1_labels, train2_labels)


def test_test_set_size():
    """The test set size should be 10k."""
    mnist = MNISTLoader(10, 0)
    assert mnist.test_set_size == 10000


def test_train_set_size():
    """The training set size should be 60k."""
    mnist = MNISTLoader(10, 0)
    assert mnist.train_set_size == 60000

def test_train_loss_loader():
    """Should return randum subset of training set.""" 
    mnist = MNISTLoader(1000, 0)
    samples = 0
    for (inputs, labels) in mnist.train_loss_loader():
        samples += labels.size()[0]
    assert samples == mnist.test_set_size
