## Quick start

* Required: Python@3.12
* Project use pipenv to manage library
* Project use npm to run command

```bash
  pip install pipenv
```

* Clone project from github. 
```bash
  git clone <repo-name>
  cd <repo-name>
  npm run download
```

* If you already install dependencies. Run bash below to access virtual enviroment
```bash
  npm run env
```

* Run project
* Create .env file in root folder. Then copy .env.example patse into ,env inside Apis sub folder

```bash
  npm run dev
```

* Seeding

```bash
  npm run seed
```

* Unix OS delete migration

```bash
  find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
```

* You can use Bun to run faster