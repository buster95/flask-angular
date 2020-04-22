# Angular Build on Python with Flask

## How to prepare the project
* first you need to install pipenv
```bash
> pip install pipenv
```

* then you can install all local packages
```bash
> pipenv install
```

* after you need to enter in the virtual enviroment
```bash
> pipenv shell
```

## How to run
* just run next command:
```bash
> flask run
```


## Others Commands

### Install Packages 
* install packages for `production` enviroment
```bash
pipenv install <package_name>
```

* install packages for `development` enviroment
```bash
pipenv install -d <package_name> 
pipenv install --dev <package_name> 
```

* install packages from `requirements.txt`
```bash
pipenv install -r <file_name.ext>
```

### Uninstall Packages
* uninstall packages
> for verbose mode you can add `-v` options or use `--verbose`
```bash
pipenv uninstall <package_name> 
pipenv uninstall -v <package_name> 
pipenv uninstall --verbose <package_name>
```

* uninstall only `development` packages
> for verbose mode you can add `-v` options or use `--verbose`
```bash
pipenv uninstall <package_name> 
pipenv uninstall -v <package_name> 
pipenv uninstall --verbose <package_name>
```