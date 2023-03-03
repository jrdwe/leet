
# runtime: O(nk * nlogk)
# space  : O(nk)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        graph, owner = collections.defaultdict(set), {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                owner[email] = name
                graph[email].add(acc[1])
                graph[acc[1]].add(email)

        out, seen = [], set()
        for email in graph:
            if email not in seen:
                stack, emails = [email], []
                seen.add(email)

                while stack:
                    n = stack.pop()
                    emails.append(n)
                    for edge in graph[n]:
                        if edge not in seen:
                            stack.append(edge)
                            seen.add(edge)

                out.append([owner[email]] + sorted(emails))

        return out
