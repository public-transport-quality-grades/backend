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

  backend = with python36.pkgs;
    buildPythonPackage {
      name = "backend";
      doCheck = false;
      src = ./.;
      propagatedBuildInputs = [ flask geojson ];
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
  