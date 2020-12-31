# Twitter BERT Visualizer
![Python](https://img.shields.io/badge/python-v3.6.9-blue.svg) ![Pytorch](https://img.shields.io/badge/PyTorch-v1.7.0-blueviolet) ![cuda](https://img.shields.io/badge/CUDA-v10.1-green) ![transformers](https://img.shields.io/badge/transformers-v3.5.1-blue)
---

### Steps: 
---
Run `setup.sh` to download and install the required packages
```bash
bash setup.sh
````
Add your twitter API keys in a file called `twitterAPIkeys.json` in the `src` folder, in the following format:
```json
{
	"API key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"API secret key" : "xxxxxxxxxxxxxxxxxxxx",
	"Access token": "xxxxxxxxxxxxxxxxxxxxxxx",
	"Access token secret": "xxxxxxxxxxxxxxxx"
}
```

### Generating a plot:
___
```bash
cd src
python main.py "seach_term" [-n number_of_tweets]
```
Make sure you are in the `src` folder. Run `main.py`, for example `python main.py "#Covid" -n 500`. An output file `plot.html` will be generated in the `output` folder. Hovering on the points shows you the tweet. The size of the points will be proportional to the number of the likes on the tweet.
### Sample plot:
___
As the plot is interactive and requires javascript, it cannot embedded in this README. To see a generated plot use the following link, hovering on the points shows you the tweet: [Sample Plot](https://keen-pike-0f2ba8.netlify.app/).
