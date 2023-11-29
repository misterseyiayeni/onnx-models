
# labels: name::falcon author::transformers task::Generative_AI license::apache-2.0
from turnkeyml.parser import parse
from transformers import FalconModel, AutoConfig
import torch

# Parsing command-line arguments
pretrained, batch_size, max_seq_length = parse(
    ["pretrained", "batch_size", "max_seq_length"]
)

# Model and input configurations
if pretrained:
    model = FalconModel.from_pretrained("Rocketknight1/falcon-rw-1b")
else:
    config = AutoConfig.from_pretrained("Rocketknight1/falcon-rw-1b")
    model = FalconModel(config)

# Make sure the user's sequence length fits within the model's maximum
assert max_seq_length <= model.config.max_position_embeddings


inputs = {
    "input_ids": torch.ones(batch_size, max_seq_length, dtype=torch.long),
    "attention_mask": torch.ones(batch_size, max_seq_length, dtype=torch.float),
}


# Call model
model(**inputs)
    