from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

from edward.util import log_sum_exp

class test_log_sum_exp_class(tf.test.TestCase):

    def test_log_sum_exp_1d(self):
        with self.test_session():
            x = tf.constant([-1.0, -2.0, -3.0, -4.0])
            self.assertAllClose(log_sum_exp(x).eval(), 
                                -0.5598103014388045)
            
    def test_log_sum_exp_2d(self):
        with self.test_session():
            x = tf.constant([[-1.0], [-2.0], [-3.0], [-4.0]])
            self.assertAllClose(log_sum_exp(x).eval(), 
                                -0.5598103014388045)             

    def test_all_finite_raises(self):
        with self.test_session():
            x = np.inf * tf.constant([-1.0, -2.0, -3.0, -4.0])
            with self.assertRaisesOpError('Inf'):
                log_sum_exp(x).eval()
            x = tf.constant([-1.0, np.nan, -3.0, -4.0])
            with self.assertRaisesOpError('NaN'):
                log_sum_exp(x).eval()                

if __name__ == '__main__':
    tf.test.main()
