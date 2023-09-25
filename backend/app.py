import os
os.kill(os.getpid(), 9)

import locale
locale.getpreferredencoding = lambda: "UTF-8"

from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig, pipeline
import torch
from accelerate import Accelerator

import os
import string
import random
import logging
import math

from flask import Flask, jsonify, request, send_from_directory
from flask_ngrok import run_with_ngrok



model_name="codellama/CodeLlama-7b-Instruct-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
pipeline = pipeline(
    "text-generation",
    model=model_name,
    torch_dtype=torch.float16,
    device_map={"": Accelerator().process_index},
    trust_remote_code=True
)

class LLM:
  def __init__(self):
    self.pipeline = pipeline
    self.tokenizer = tokenizer

  def generate(self, prompt):
    sequences = self.pipeline(
        prompt,
        do_sample=True,
        top_k=40,
        num_return_sequences=1,
        eos_token_id=self.tokenizer.eos_token_id,
        max_length=10000,
    )
    return sequences[0]['generated_text']
  
  llm = LLM()

  #if you're using google colab , un comment this line below and execute it:
  #from google.colab.output import eval_js
  #print(eval_js("google.colab.kernel.proxyPort(5000)"))



app = Flask(__name__)
run_with_ngrok(app)

@app.route('/generate', methods=['POST'])
def intiator():
  json = request.json

  prompt = json['prompt']
  print("Generating results")

  o = llm.generate(prompt)
  o = o[o.index("[/INST]")+len("[/INST]"):].strip()

  return jsonify({ "output": o })

app.run()



