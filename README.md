django-academy-2025/
│
├── docs/
│   ├── index.md
│   │
│   ├── cbvs/
│   │   ├── 00_introducao.md
│   │   ├── 01_fundamental.md
│   │   ├── 02_basico.md
│   │   ├── 03_intermediario.md
│   │   ├── 04_avancado.md
│   │   ├── 05_profissional.md
│   │   ├── 06_senior.md
│   │   └── 07_referencia_geral.md
│   │
│   ├── fbvs/
│   │   ├── 00_introducao.md
│   │   ├── 01_basico.md
│   │   ├── 02_intermediario.md
│   │   └── 03_avancado.md
│   │
│   ├── drf/
│   │   ├── 00_intro_drf.md
│   │   ├── 01_apiview.md
│   │   ├── 02_generic_api.md
│   │   ├── 03_viewsets.md
│   │   ├── 04_auth_jwt.md
│   │   └── 05_permissions.md
│   │
│   ├── docker/
│   │   ├── guia_docker.md
│   │   ├── compose_explicado.md
│   │   ├── deploy_docker.md
│   │   └── stacks_comuns.md
│   │
│   ├── cli/
│   │   ├── introducao_cli.md
│   │   ├── comandos_basicos.md
│   │   ├── como_criar_cli.md
│   │   └── cli_avancado.md
│   │
│   ├── projetos/
│   │   ├── 01_crud_completo.md
│   │   ├── 02_dashboard_cbv.md
│   │   ├── 03_auth_jwt_api.md
│   │   ├── 04_calendario_htmx.md
│   │   ├── 05_fullstack_react.md
│   │   └── 06_asset_manager.md
│   │
│   ├── testes/
│   │   ├── pytest_intro.md
│   │   ├── testando_cbvs.md
│   │   ├── testando_apis.md
│   │   └── factories_e_fixtures.md
│   │
│   ├── materiais/
│   │   ├── cheatsheet_cbvs.md
│   │   ├── cheatsheet_fbv.md
│   │   ├── cheatsheet_drf.md
│   │   ├── glossario_django.md
│   │   ├── roadmap_django_2025.md
│   │   └── design_patterns_django.md
│   │
│   └── index.md
│
│
├── src/
│   ├── cbvs/
│   │   ├── backend/
│   │   │   ├── manage.py
│   │   │   ├── core/
│   │   │   │   ├── settings/
│   │   │   │   │   ├── base.py
│   │   │   │   │   ├── dev.py
│   │   │   │   │   └── prod.py
│   │   │   │   ├── urls.py
│   │   │   │   ├── wsgi.py
│   │   │   │   ├── asgi.py
│   │   │   │   └── __init__.py
│   │   │   └── apps/
│   │   │       └── exemplo/ (CRUD demonstrativo)
│   │   │
│   │   ├── templates/
│   │   └── tests/
│   │
│   ├── fbvs/
│   │   ├── backend/
│   │   └── templates/
│   │
│   ├── drf/
│   │   ├── backend/
│   │   └── api/
│   │
│   ├── shared/
│   │   ├── mixins/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── components/
│   │   └── templates/
│   │
│   └── frontends/
│       ├── htmx/
│       ├── tailwind/
│       ├── react/
│       └── next/
│
│
├── cli/
│   ├── main.py
│   ├── __init__.py
│   ├── commands/
│   │   ├── newproject.py
│   │   ├── newapp.py
│   │   ├── generate_docs.py
│   │   └── check_env.py
│   └── utils/
│
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-entrypoint.sh
│   ├── nginx/
│   ├── postgres/
│   └── redis/
│
│
├── scripts/
│   ├── init.sh
│   ├── setup_poetry.sh
│   ├── lint.sh
│   ├── build_docs.sh
│   ├── run_tests.sh
│   └── backup_db.sh
│
│
├── mkdocs.yml
├── README.md
├── .gitignore
└── LICENSE
