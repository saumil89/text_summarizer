import os
from transformers import AutoTokenizer
from textSummarizer.logging import logger
from datasets import load_dataset, load_from_disk
from pathlib import Path
from textSummarizer.entity import DataTransformationConfig

class DataTransfomation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, examples):
        input_encoding = self.tokenizer(examples['dialogue'], truncation=True, padding=True, max_length=self.config.max_input_length)

        with self.tokenizer.as_target_tokenizer():
            target_encoding = self.tokenizer(examples['summary'], truncation=True, padding=True, max_length=self.config.max_output_length)

        return {
            'input_ids': input_encoding['input_ids'],
            'attention_mask': input_encoding['attention_mask'],
            'labels': target_encoding['input_ids']        
        }
    
    def convert(self):
        data_samsum = load_dataset(self.config.data_path)
        data_samsum_pt = data_samsum.map(self.convert_examples_to_features, batched=True)
        data_samsum_pt.save_to_disk(Path(f'{self.config.root_dir}/samsum_dataset'))