# 📝 Automated Detection and Recognition of Grammatical Errors  

This project implements a grammar error correction system using **GECToR (Grammatical Error Correction: Tag, Not Rewrite)** with **RoBERTa** as the transformer backbone.  
It detects and corrects grammatical errors in text efficiently, making it useful for academic, professional, and research applications.  

---

## 🚀 Features
- Transformer-based grammar error detection & correction  
- Lightweight and fast compared to traditional seq2seq approaches  
- Preprocessing and utility scripts for custom data  
- Extendable for fine-tuning on new datasets  

---

## ⚙️ Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/Srishti-951245/Automated-Detection-and-Recognition-of-Grammatical-Errors.git
   cd Automated-Detection-and-Recognition-of-Grammatical-Errors

The following command installs all necessary packages:
```.bash
pip install -r requirements.txt
```
The project was tested using Python 3.7.

## Datasets
All the public GEC datasets used in the paper can be downloaded from [here](https://www.cl.cam.ac.uk/research/nl/bea2019st/#data).<br>
Synthetically created datasets can be generated/downloaded [here](https://github.com/awasthiabhijeet/PIE/tree/master/errorify).<br>
To train the model data has to be preprocessed and converted to special format with the command:
```.bash
python utils/preprocess_data.py -s SOURCE -t TARGET -o OUTPUT_FILE
```
## Pretrained models
<table>
  <tr>
    <th>Pretrained encoder</th>
    <th>Confidence bias</th>
    <th>Min error prob</th>
    <th>CoNNL-2014 (test)</th>
    <th>BEA-2019 (test)</th>
  </tr>
  <tr>
    <td>BERT <a href="https://grammarly-nlp-data-public.s3.amazonaws.com/gector/bert_0_gectorv2.th">[link]</a></td>
    <td>0.1</td>
    <td>0.41</td>
    <td>61.0</td>
    <td>68.0</td>
  </tr>
  <tr>
    <td>RoBERTa <a href="https://grammarly-nlp-data-public.s3.amazonaws.com/gector/roberta_1_gectorv2.th">[link]</a></td>
    <td>0.2</td>
    <td>0.5</td>
    <td>64.0</td>
    <td>71.8</td>
  </tr>
  <tr>
    <td>XLNet <a href="https://grammarly-nlp-data-public.s3.amazonaws.com/gector/xlnet_0_gectorv2.th">[link]</a></td>
    <td>0.2</td>
    <td>0.5</td>
    <td>63.2</td>
    <td>71.2</td>
  </tr>
</table>





 


## Model inference
To run your model on the input file use the following command:
```.bash
python predict.py --model_path MODEL_PATH [MODEL_PATH ...] \
                  --vocab_path VOCAB_PATH --input_file INPUT_FILE \
                  --output_file OUTPUT_FILE
```
Among parameters:
- `min_error_probability` - minimum error probability (as in the paper)
- `additional_confidence` - confidence bias (as in the paper)
- `special_tokens_fix` to reproduce some reported results of pretrained models

