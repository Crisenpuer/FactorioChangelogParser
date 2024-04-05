import os

file = open('changelog.txt', 'r')
changelog_in = []
for line in file:
    changelog_in.append(line)
file.close()

if not os.path.exists("changelog.txt"):
    print("changelog.txt does not exist")
else:
    if os.path.exists("CHANGELOG.md"):
        os.remove("CHANGELOG.md")
    outfile = open("CHANGELOG.md", "x")

    skip_next_line = False
    changelog_out = []
    versions_parsed = 0


    for i in range(len(changelog_in)):
        ##### Uncomment for debug process #####
        # print(f'{i}/{len(changelog_in)-1}: {changelog_in[i]}')
        entry:str = changelog_in[i].rstrip('\n')
        if skip_next_line:
            skip_next_line = False

        else:
            if len(changelog_out) == 0 and entry.startswith("Version:"):
                formatted_line = entry.replace(':','')
                print(f'Parsing {(formatted_line.lower()).replace("  ", " ")}')
                versions_parsed += 1
                changelog_out.append(f'# {formatted_line} ')
                if not 'Date:' in changelog_in[i+1]:
                    changelog_out.append(f' [date unknown]\n')

            elif entry.startswith("Version:"):
                formatted_line = entry.replace(':','')
                print(f'Parsing {formatted_line.lower()}')
                versions_parsed += 1
                changelog_out.append(f'\n\n# {formatted_line} ')
                if not 'Date:' in changelog_in[i+1]:
                    changelog_out.append(f' [date unknown]\n')

            elif entry.startswith('Date:'):
                formatted_line = entry.lstrip('Date: ')
                formatted_line = formatted_line.replace('.','-')
                if 'unknown' in formatted_line:
                    formatted_line == 'date unknown'
                changelog_out.append(f'[{formatted_line}]\n')

            elif entry.startswith('  ') and entry.endswith(':'):
                changelog_out.append(f'\n### {entry.lstrip("  ")}\n')

            elif entry.startswith('    - '):
                formatted_line = entry.replace('    ', '  ')
                changelog_out.append(f'{formatted_line}\n')

    for ent in changelog_out:
        outfile.write(ent)

    outfile.close()
    if versions_parsed == 1:
        print(f"\nParsed {len(changelog_in)-1} lines in 1 version")
    else:
        print(f"\nParsed {len(changelog_in)-1} lines in {versions_parsed} versions")