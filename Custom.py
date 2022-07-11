import sys
sys.path.append("E:\dev\MORE_PIPELINE\PIPELINE_BASE")
from PLE_CORE.job import jobs_env,  JobsFactory
class CustomDate(jobs_env.JobsEnv):
    def __init__(self,type,factory : JobsFactory):
        super().__init__()
        self.type = type  #car type
        self.factory = factory
    #     self.set_factory()
    #
    #
    # def set_factory(self):
    #     a = runtime_env.RuntimeEnv()
    #     a.set_pipeline_factory(self.factory)
    #     a.set_dcc_name("by a car")



