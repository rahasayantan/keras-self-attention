import keras
from keras_self_attention import SelfAttention
from .util import TestMaskShape


class TestMask(TestMaskShape):

    def test_return_attention(self):
        attention = SelfAttention(return_attention=True,
                                  kernel_regularizer=keras.regularizers.l2(1e-4),
                                  bias_regularizer=keras.regularizers.l1(1e-4),
                                  name='Attention')
        self.check_mask_shape(attention)
