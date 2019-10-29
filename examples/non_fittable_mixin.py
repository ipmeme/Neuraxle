"""
Create Pipeline Steps in Neuraxle that doesn't Require Fitting (Non-Fittable) or/nor Transforming (Non-Transformable)
========================================================================================================================

If a pipeline step doesn't need to be fitted and only transforms data (e.g.: taking the logarithm of the data),
then you can inherit from the NonFittableMixin as demonstrated here, which will override the fit method properly
for you. You can also use a NonTransformableMixin if your step doesn't transform anything, which is rarer. If your step
simply just does nothing to the data, then you could even use the Identity class of Neuraxle, which is simply a class
that inherits from both the NonFittableMixin, the NonTransformableMixin, and BaseStep.

Mixins are an old Object Oriented Programming (OOP) design pattern that resurfaces when designing
Machine Learning Pipelines. Those are add-ons to classes to implement some methods in some specific ways already.
A mixin doesn't inherit from BaseStep itself, because we can combine many of them in one class. However, a mixin must
suppose that the object that inherits from the mixin also inherits from it's base class. Here, our base class is the
BaseStep class.

..
    Copyright 2019, Neuraxio Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

..
    Thanks to Umaneo Technologies Inc. for their contributions to this Machine Learning
    project, visit https://www.umaneo.com/ for more information on Umaneo Technologies Inc.

"""
import numpy as np

from neuraxle.base import NonTransformableMixin, NonFittableMixin, Identity, BaseStep
from neuraxle.pipeline import Pipeline


class NonTransformableStep(NonTransformableMixin, BaseStep):
    """
    Transform method is automatically implemented as returning data inputs as it is.
    Please make your steps inherit from NonTransformableMixin, when they don't need any transformations.
    Also, make sure that BaseStep is the last step you inherit from.
    """

    def fit(self, data_inputs, expected_outputs=None) -> 'NonTransformableStep':
        # insert your fit code here
        print('data_inputs: {0}'.format(data_inputs))
        print('expected_outputs: {0}'.format(expected_outputs))
        return self


class NonFittableStep(NonFittableMixin, BaseStep):
    """
    Fit method is automatically implemented as changing nothing.
    Please make your steps inherit from NonFittableMixin, when they don't need any transformations.
    Also, make sure that BaseStep is the last step you inherit from.
    """

    def transform(self, data_inputs):
        # insert your transform code here
        print('data_inputs: {0}'.format(data_inputs))
        return self, data_inputs

    def inverse_transform(self, processed_outputs):
        # insert your inverse transform code here
        return processed_outputs


def main():
    p = Pipeline([
        NonFittableStep(),
        NonTransformableStep(),
        Identity()
    ])

    p = p.fit(np.array([0, 1]), np.array([0, 1]))
    outputs = p.transform(np.array([0, 1]))


if __name__ == "__main__":
    main()
