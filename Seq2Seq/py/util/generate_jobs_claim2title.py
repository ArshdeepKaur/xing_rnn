import os
import sys
from job import Jobs


def standalone():
    
    j = Jobs("claim2title",hours = 10, machine_type = "gpu4", per_gpu = 4)
    grids = {"name":["c2t"],
             "batch_size":[128],
             "size": [500],
             "dropout":[0.8],
             "learning_rate":[0.05,0.01,0.005],
             "n_epoch":[20],
             "num_layers":[2],
             "attention":[True],
             "from_vocab_size":[200000],
             "to_vocab_size":[40000],
             "min_source_length":[0],
             "max_source_length":[200],
             "min_target_length":[0],
             "max_target_length":[100],
             "n_bucket":[10],
             "optimizer":["adam"],
             "learning_rate_decay_factor":[1.0],
             "N":["00000"],
             "attention_style":["additive"],
             "attention_scale":[False],
             "preprocess_data":[False],
             "checkpoint_steps":[0]
    }

    beams = [12]
    
    j.generate(grids,beams)

        

def distributed():
    
    j = Jobs("claim2title",hours = 10, machine_type = "gpu4")
    grids = {"name":["c2t"],
             "batch_size":[128],
             "size": [500],
             "dropout":[0.5, 0.8],
             "learning_rate":[1.0],
             "n_epoch":[20],
             "num_layers":[1,2],
             "attention":[True, False],
             "from_vocab_size":[200000],
             "to_vocab_size":[40000],
             "min_source_length":[0],
             "max_source_length":[200],
             "min_target_length":[0],
             "max_target_length":[100],
             "n_bucket":[10],
             "optimizer":["sgd"],
             "learning_rate_decay_factor":[0.5],
             "NN":["00000,11111,22222,33333"],
             "attention_style":["additive"],
             "attention_scale":[False],
             "preprocess_data":[True],
             "checkpoint_steps":[0]
    }

    beams = [12]
    
    j.generate(grids,beams,dist=True)

        

if __name__ == "__main__":
    distributed()
    #standalone()

    

    
    
