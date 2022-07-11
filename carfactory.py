from PIPELINE_BASE.PLE_CORE.job import jobs_factory
from createcar.builder.builder_Acar.build_Acar import CreateA


class CarFactory(jobs_factory.JobsFactory):
    def creatCarBuilder(self,context):
        if context.CustomDate.type == "A":
            from builder.builder_Acar import build_Acar
            return build_Acar.CreateA(context)


