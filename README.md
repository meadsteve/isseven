# Isseven

For too long we've struggled to know if something isseven. Now thanks to the power of this API we can be sure if **it** isseven.

Here are some example usages:

```bash
curl {{HOSTED_URL}}/is/6
# {"isseven":false,"explanation":"We tried. This doesn't seem to be seven"}%   

curl {{HOSTED_URL}}/is/seven
# {"isseven":true,"explanation":"That was seven in english"}

curl {{HOSTED_URL}}/is/qqqqqqq
# {"isseven":true,"explanation":"It was q repeated 7 times"}

curl {{HOSTED_URL}}/is/3+4
# {"isseven":true,"explanation":"According to the power of maths that is 7"}
```

## Support

Full API docs can be found at [{{HOSTED_URL}}/docs]({{HOSTED_URL}}/docs)

Issues tracked on GitHub [meadsteve/isseven](https://github.com/meadsteve/isseven/issues)

## Running locally
Requires python 3.8 or higher to be installed.

*  `git clone git@github.com:meadsteve/isseven.git` 
*  `cd isseven`
*  `pipenv install` (you'll need to do `pip install pipenv` if you don't already have this available)
*  `./run.sh`
