class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block_comment = False
        result = []
        current_line = []

        for i in range(len(source)):
            line = source[i]
            j = 0

            while j < (len(line)):
                if block_comment:
                    if j < len(line) - 1 and line[j] == "*" and line[j + 1] == "/":
                        block_comment = False
                        j += 1

                else:  # not in block comment mode
                    if line[j] == "/" and j < len(line) - 1:
                        if line[j + 1] == "*":
                            block_comment = True
                            j += 1

                        elif line[j + 1] == "/":  # line comment
                            break

                        else:
                            current_line.append(line[j])

                    else:
                        current_line.append(line[j])

                j += 1

            if not block_comment:
                line = "".join(current_line)
                if line:
                    result.append(line)
                current_line = []

        return result
