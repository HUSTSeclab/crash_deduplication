# crash_deduplication

- Ground truth dataset of our NDSS paper[1]
- Scripts to manipulate this ground truth dataset

## Dataset format

|--------|----------------------------------------|-----|----------------|
|Patch   |BUG id                                  |Title|Affected Reasons|
|cd443f1e|502c872feb9bbb5ad6494c349c7faa87a9f1777b|[general protection fault in strlen](https://syzkaller.appspot.com/bug?id=502c872feb9bbb5ad6494c349c7faa87a9f1777b)|Memory Dynamics|
|cd443f1e|5ea2c9ac96fc3c1da4d7ee9572c8c7ed229f1b13|[KASAN: stack-out-of-bounds Read in __nla_put](https://syzkaller.appspot.com/bug?id=5ea2c9ac96fc3c1da4d7ee9572c8c7ed229f1b13)||

[1] [An In-depth Analysis of Duplicated Linux Kernel Bug Reports"](https://mudongliang.github.io/files/papers/NDSS_deduplication.pdf)
