# Applying DrQA, a question answering system on an arbitary website

A few scripts and code snippets to create a simple question answering system for any website.

We assume that you are familiar with basic bash and linux.
If you are on windows, you can either use Ubuntu Bash (windows store) or modify the bash scripts to work on windows cmd.

## Requirements:

* Checkout DrQA into `~/DrQA-Demo`  (https://github.com/facebookresearch/DrQA)
* follow installation steps from DrQA
* checkout https://github.com/ArlindNocaj/drqa-demo.git into `~/DrQA-Demo/handson`


## Main Steps

* step 1: modify `downloadWebpage.sh`: so that it contains the webpage you want to have, e.g. replace openai.com

* step 2 : execute `./downloadWebpage.sh`: downloads a webpage recursively. feel free to stop it at some point if it takes too long

* step 3: convert the downloaded pages to the right format: `./convert_html.sh ./openai.com`. This also creates a ngram based index for the text of your page.

* step 4: start your system: `./start_webpage.sh`