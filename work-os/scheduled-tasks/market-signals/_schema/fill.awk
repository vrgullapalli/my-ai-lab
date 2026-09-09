# usage: awk -f fill.awk deltas.txt schema.md
FNR==NR {
  if ($0 ~ /^::[A-Z_]+::$/) { slot = substr($0, 3, length($0)-4); val[slot] = ""; seen[slot]=1; first[slot]=1; next }
  if (slot != "") { if (first[slot]) { val[slot] = $0; first[slot]=0 } else { val[slot] = val[slot] "\n" $0 } }
  next
}
{
  line = $0
  while (match(line, /\{\{[A-Z_]+\}\}/)) {
    name = substr(line, RSTART+2, RLENGTH-4)
    if (!(name in seen)) { print "MISSING SLOT: " name > "/dev/stderr"; repl = "" } else { repl = val[name] }
    line = substr(line, 1, RSTART-1) repl substr(line, RSTART+RLENGTH)
  }
  print line
}
