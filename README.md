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
```

## Support

Full API docs can be found at [{{HOSTED_URL}}/docs]({{HOSTED_URL}}/docs)

Issues tracked on GitHub [meadsteve/isseven](https://github.com/meadsteve/isseven/issues)
