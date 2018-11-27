from abc import ABC, abstractmethod

class MediationProcess(ABC):
    """description of class"""

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def validate(self, dataframe):
        pass

    @abstractmethod
    def aggregate(self, validated_df):
        pass


    
