import sys, getopt

import tensorflow as tf

def rename(checkpoint_dir, prefix, replace_substr1, replace_substr2):
    checkpoint = tf.train.get_checkpoint_state(checkpoint_dir)
	
    with tf.Session() as sess:
	    #check all variable in the checkpoint
        for var_name, _ in tf.contrib.framework.list_variables(checkpoint_dir):
		
            # Load the variable in the checkpoint
            var = tf.contrib.framework.load_variable(checkpoint_dir, var_name)

            # Check previous and update the string (replace and prefix)
            new_name = var_name
            if None not in [replace_substr1, replace_substr2]:
                new_name = new_name.replace(replace_substr1, replace_substr2)
            if prefix:
                new_name = prefix + new_name


            print('Renaming %s to %s.' % (var_name, new_name))
            # Update the name of the variable in the update list
            var = tf.Variable(var, name=new_name)

        
        # Run the session
        print('Save in checkpoint %s (if your model is quite deep, it will take few sencods)' % checkpoint.model_checkpoint_path)
        saver = tf.train.Saver()
        sess.run(tf.global_variables_initializer())
		# Save the model with new names
        saver.save(sess, checkpoint.model_checkpoint_path)
        
        

def main():
# you have to change these 4 values
    checkpoint_dir = 'path_of_your_checkpoint'
    replace_substr1 = 'string1'
    replace_substr2 = 'string2'
    prefix = 'prefix'

    rename(checkpoint_dir, prefix, replace_substr1, replace_substr2)


if __name__ == '__main__':
    main()

