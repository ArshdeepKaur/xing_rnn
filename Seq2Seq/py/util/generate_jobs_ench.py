import os
import sys
from job import Jobs

def distributed1():
    
    j = Jobs("ench",hpc_hours = 100, hpc_machine_type = "gpu2", per_gpu = True, num_gpus_per_task = 1, num_gpus_per_machine = 6, root_dir = "/home/specifio/xingshi/Seq2Seq")
    grids = {"name":["ench"],
             "batch_size":[128],
             "size": [1000],
             "dropout":[0.7],
             "learning_rate":[0.35],
             "n_epoch":[40],
             "num_layers":[2],
             "attention":[True],
             "from_vocab_size":[40000],
             "to_vocab_size":[40000],
             "min_source_length":[0],
             "max_source_length":[50],
             "min_target_length":[0],
             "max_target_length":[50],
             "n_bucket":[10],
             "optimizer":["sgd"],
             "learning_rate_decay_factor":[0.5],
             "N":["00000"],
             "attention_style":["additive"],
             "attention_scale":[False],
             "preprocess_data":[True],
             "checkpoint_steps":[0],
    }

    decode_grids = {
        "beam_size":[12],
        "max_ratio":[1.5],
        "min_ratio":[0.5],
        "max_source_length":[400]
    }
    
    
    j.generate(grids,decode_grids,dist=False)

def distributed2():
    
    j = Jobs("chen",hpc_hours = 100, hpc_machine_type = "gpu2", per_gpu = True, num_gpus_per_task = 1, num_gpus_per_machine = 6, root_dir = "/home/specifio/xingshi/Seq2Seq")
    grids = {"name":["chen"],
             "batch_size":[128],
             "size": [1000],
             "dropout":[0.9],
             "learning_rate":[0.35],
             "n_epoch":[40],
             "num_layers":[2],
             "attention":[True],
             "from_vocab_size":[40000],
             "to_vocab_size":[40000],
             "min_source_length":[0],
             "max_source_length":[50],
             "min_target_length":[0],
             "max_target_length":[50],
             "n_bucket":[10],
             "optimizer":["sgd"],
             "learning_rate_decay_factor":[0.5],
             "N":["00000"],
             "attention_style":["additive","multiply"],
             "attention_scale":[False],
             "preprocess_data":[True],
             "checkpoint_steps":[0],
    }

    decode_grids = {
        "beam_size":[12],
        "max_ratio":[1.5],
        "min_ratio":[0.5],
        "max_source_length":[400]
    }
    
    
    j.generate(grids,decode_grids,dist=False)


        

if __name__ == "__main__":
    #distributed()
    distributed1()
    distributed2()
    #standalone()
