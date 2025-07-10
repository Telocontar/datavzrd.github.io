# Datavzrd

Links:
 * [datavzrd](https://github.com/datavzrd/datavzrd)
 * [Tutorial](https://github.com/datavzrd/datavzrd.github.io)
 * [Documentation](https://datavzrd.github.io/docs/)

Repo has been run on [Gitpod](https://gitpod.io/).

Create datavzrd report using 
```bash
datavzrd config.yaml --output example-report --overwrite-output
```
for the provided data or
```bash
datavzrd config_perimyo.yaml --output perimyo-report --overwrite-output
```
for the synthetic data.

Create suggestions using
```bash
datavzrd suggest -f data/perimyo_combined.csv -s $',' > perimyo_datavzrd_suggestion.yaml
```

# Gitpod
Run Jupyter notebook:
```
jupyter notebook --no-browser --port=8888 --ip=0.0.0.0 --NotebookApp.token=''
```

