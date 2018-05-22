with import <nixpkgs> {}; let
  geojson = with python36.pkgs;
    buildPythonPackage {
      name = "geojson-2.3.0";
      doCheck = false;
      src = fetchurl {
        url = "https://pypi.python.org/packages/ee/5b/8785c562d2bc910a5effada38d86925afa3d1126ddb3d0770c8a84be8baa/geojson-2.3.0.tar.gz";
        sha256 = "06ihcb8839zzgk5jcv18kc6nqld4hhj3nk4f3drzcr8n8893v1y8";
      };
    };

  apispec = with python36.pkgs;
    buildPythonPackage {
    name = "apispec-0.37.0";
    doCheck = false;
    propagatedBuildInputs = [
      pyyaml
    ];
    src = fetchurl {
      url = "https://files.pythonhosted.org/packages/d3/20/7af547f84c131a6a856146a5cf2c341f99250293aa87ef56668f88d705b3/apispec-0.37.0.tar.gz";
      sha256 = "1ly6r56kr1r9ggx9fr1x5x42awmsr4kdmvlv7bmyxb1bkri2xsbm";
    };
  };

  flasgger = with python36.pkgs;
    buildPythonPackage {
    name = "flasgger-0.8.3";
    doCheck = false;
    propagatedBuildInputs = [
      flask
      pyyaml
      jsonschema
      mistune
      six
    ];
    src = fetchurl {
      url = "https://files.pythonhosted.org/packages/61/40/9874c6235c832e34d4ba208a90d92b7fca2e73ea10b52b7e6fcc2ccfe384/flasgger-0.8.3.tar.gz";
      sha256 = "0c7r5iiz92kfs70s82m6sc3yp742z0xk1g6n587d6fn48s77km70";
    };
  };

  backend = with python36.pkgs;
    buildPythonPackage {
      name = "backend";
      doCheck = false;
      src = ./.;
      propagatedBuildInputs = [ flask marshmallow flasgger apispec  geojson ];
    };
in
(python3.withPackages (
  pkgs: with pkgs;
  [
    backend
    # dev requirements
    pytest
    pytest-sugar
    pytestcov
  ]
)).env
  