# This code is part of Qiskit.
#
# (C) Copyright IBM 2020, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

""" Test Breast Cancer """

import unittest
from test import QiskitMachineLearningTestCase
import json
import numpy as np
from qiskit_machine_learning.datasets import breast_cancer


class TestBreastCancer(QiskitMachineLearningTestCase):
    """ Breast Cancer tests."""

    def test_breast_cancer(self):
        """Breast Cancer test."""

        input_file = self.get_resource_path('sample_train.breast_cancer',
                                            'datasets')
        with open(input_file) as file:
            sample_train_ref = json.load(file)

        input_file = self.get_resource_path('training_input.breast_cancer',
                                            'datasets')
        with open(input_file) as file:
            training_input_ref = json.load(file)

        input_file = self.get_resource_path('test_input.breast_cancer',
                                            'datasets')
        with open(input_file) as file:
            test_input_ref = json.load(file)

        sample_train, training_input, test_input, class_labels = breast_cancer(training_size=20,
                                                                               test_size=10,
                                                                               n=2,
                                                                               plot_data=False)
        np.testing.assert_allclose(sample_train.tolist(), sample_train_ref, rtol=1e-04)
        for key, _ in training_input.items():
            np.testing.assert_allclose(training_input[key].tolist(),
                                       training_input_ref[key], rtol=1e-04)
        for key, _ in test_input.items():
            np.testing.assert_allclose(test_input[key].tolist(), test_input_ref[key], rtol=1e-04)
        np.testing.assert_array_equal(class_labels, list(training_input.keys()))


if __name__ == '__main__':
    unittest.main()
