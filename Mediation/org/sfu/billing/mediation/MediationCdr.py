from billing.mediation import MediationProcess

class MediationCdr(MediationProcess):
    """description of class"""

    def __init__(self, df):
        self.df = df

    def validate(self, dataframe):
        print("Validate method....")
        return "validation"

    def aggregate(self, dataframe):
        print("Aggregated frame")
        return "Aggregation"

    def execute(self, mapped_frame):
        validated_frames = validate(self, mapped_frame)
        aggregated_frames = aggregate(validated_frames)
        return aggregated_frames

x= MediationCdr(10)
x.aggregate("test")





