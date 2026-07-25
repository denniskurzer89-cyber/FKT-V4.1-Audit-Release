#!/bin/bash
echo "FKT P2 Setup"
pip install cobaya numpy scipy matplotlib getdist pyyaml

if [ ! -d "class_public" ]; then
    git clone https://github.com/lesgourg/class_public.git
    cd class_public && make -j4 && cd ..
fi

echo "✓ Setup abgeschlossen"
