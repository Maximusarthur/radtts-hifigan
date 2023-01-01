# RADTTS + HiFiGAN vocoder

🇺🇦 Join Ukrainian Text-to-Speech community: https://t.me/speech_synthesis_uk

Clone the code:

```bash
git clone https://github.com/egorsmkv/radtts-hifigan
cd radtts-hifigan
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download Ukrainian RADTTS and HiFiGAN models:

```bash
mkdir models
cd models

wget https://github.com/egorsmkv/radtts-hifigan/releases/download/v1.0/hifi_config.json
wget https://github.com/egorsmkv/radtts-hifigan/releases/download/v1.0/hifi_vocoder.pt
wget https://github.com/egorsmkv/radtts-istftnet/releases/download/v1.0/RADTTS-Lada.pt
```

Then you can inference own texts by the following command:

```bash
python3 inference.py -c config_ljs_dap.json -r models/RADTTS-Lada.pt -t test_sentences.txt --vocoder_path models/hifi_vocoder.pt --vocoder_config_path models/hifi_config.json -o results/
```
