# -*- coding: utf-8 -*-
# MIT License
# 
# Copyright (c) 2018 ZhicongYan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

def get_validator(name, config):
    if name == 'hidden_variable':
        # view the data generated from hidden variable
        from .hidden_variable import HiddenVariable
        return HiddenVariable(config)
    elif name == 'scatter_plot':
        from .scatter_plot import ScatterPlot
        return ScatterPlot(config)
    elif name == 'dataset_validator':
        from .dataset_validator import DatasetValidator
        return DatasetValidator(config)
    elif name == 'random_generate':
        from .random_generate import RandomGenerate
        return RandomGenerate(config)
    elif name == 'embedding_visualize' or name == 'tensorboard embedding':
        from .tensorboard_embedding import TensorboardEmbedding
        return TensorboardEmbedding(config)
    elif name == 'validate_segmentation':
        from .valid_segmentation import ValidSegmentation
        return ValidSegmentation(config)
    elif name == 'gan_toy_plot':
        from .gan_toy_plot import GanToyPlot
        return GanToyPlot(config)
    elif name == 'inception_score':
        from .inception_score import InceptionScore
        return InceptionScore(config)
    else:
        raise Exception("None validator named " + name)


