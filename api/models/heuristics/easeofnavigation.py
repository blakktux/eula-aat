from models.heuristic import Heuristic

# Formal 3
# Ensure ease of user navigation.
class EaseOfNavigation(Heuristic):

    @staticmethod
    def score(eula):
        name = 'Ease of Navigation'
        grade = 'NR'
        description = 'Not yet implemented'

        return {
            'name'        : name,
            'grade'       : grade,
            'description' : description,
            'score'       : -1,
            'max'         : 4,
            'reason'      : 'Not implemented'
        }