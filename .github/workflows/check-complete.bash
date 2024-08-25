@@ -1,5 +1,3 @@
#!/bin/bash
set -e
if grep -q _enter *.md; then
  echo "Replace all text having Reflections"
  exit 1
fi
