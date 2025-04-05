# Regular expressions

```bash
python3 -c "import this" > zen.txt
```
# Grep - searching for files

### Grep has parameters
- regular expression
- file to looking for

```bash
grep Beautiful zen.txt
```
- and it prints the line where the word is
- grep is case-sensitive
- "grep i" tells to grep to ignore case

### ignores case
```bash
grep -i beautiful zen.txt
```

### outputs only the word that match, not entire line
```bash
grep -o beautiful zen.txt
```

### ^ Creates a rule that matches "If" in the occurs in the beggining of line
```bash
grep ^If  zen.txt
```
### $ Creates a rule that matches "If" in the occurs in the end of line
```bash
grep idea.$  zen.txt
```

### inside a list [ow] turns into "or" operand.
```bash
echo Two too. | grep -i t[ow]o
```

### matches all the digits and ignore any other character.
```bash
echo 123?4 hello? | grep -i [:digit:]
```

### escaping $ dollar sign
```bash
echo I love $ | grep \$
```

### Only words that have two with anyone other ahead
```bash
echo Two twoo not too. $ | grep -io two*
```

### .* matches all characters in any ahead between two underscores
```bash
echo __hello__there | grep -o __.*__ # __hello__
```

```bash
echo __hi__bye_I__ | grep -o __.*__ # __hello__
```

```bash
echo __hello__there | grep -o __.*th # __hello__th
```