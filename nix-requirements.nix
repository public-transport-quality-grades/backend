with import <nixpkgs> {};
(python3.withPackages (
  pkgs: with pkgs;
  [
    flask

    # dev requirements
    pytest
    pytest-sugar
    pytestcov
  ]
)).env
  