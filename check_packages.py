import importlib.util
packages = ['reportlab', 'docx', 'PIL', 'fpdf']
for pkg in packages:
    spec = importlib.util.find_spec(pkg)
    print(pkg, bool(spec))
