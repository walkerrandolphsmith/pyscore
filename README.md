# PyScore [![Build Status](https://travis-ci.org/agguzman/pyscore.svg?branch=master)](https://travis-ci.org/agguzman/pyscore)

Collection of utility functions in Python inspired by Underscore and Lodash

Setup Virtual Environment
```
virtualenv venv --no-site-packages
```

Note: For the remaining steps windows users will find their virtual environment dependencies in
`Scripts` instead of `bin`.

Install dependencies
```
./venv/bin/pip install -r requirements.txt
```

Update dependencies
```
./venv/bin/shovel tasks.install
```

Run specs
```
./venv/bin/shovel tasks.test
```

Run single spec
```
./venv/bin/shovel tasks.testone [test filename]
```
