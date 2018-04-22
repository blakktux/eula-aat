from models.heuristic import Heuristic

# Procedural 1a
# Ensure contrast of EULA link with background on mobile devices
class MobileAccessibility(Heuristic):

    @staticmethod
    def score(eula):
        name = 'Mobile Accessibility'
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
