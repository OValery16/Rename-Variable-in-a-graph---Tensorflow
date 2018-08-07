# Rename Variable in a graph - Tensorflow

If you want to build a model that use a pretained Tensorflow model (for example, as feature extractor), you might encounter the following situation. Some names in the graph of your first model might be the same as the one of your second model. If your try to restore the weight of your first model, tensorflow will intent to update the wrong part of your final graph, causing in most of the cases some erros. 

To solve this problem, the solution is often to processed to some variable renaming. 


1. You rename manually your first model its. 
For example, ```with tf.variable_scope('generator'):``` could become ```with tf.variable_scope('generator_Model1'):```
2. You rename the variable contained in the checkpoint of your first model, using the script ```tf_rename.py``` of this project.  don't forget to update the code according your need. In the previous example, we get:

```python
    checkpoint_dir = 'checkpoint_dir'
    replace_substr1 = 'generator'
    replace_substr2 = 'generator_Model1'
	prefix = ''
```
This script will update each variable accordingly.

3. You can restore the weights of the first model from the code of your second model.
