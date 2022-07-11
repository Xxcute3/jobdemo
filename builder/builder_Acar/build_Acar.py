from PIPELINE_BASE.PLE_CORE.job import builder_base
from createcar.builder.builder_Acar.A_step1 import Astep1
from createcar.builder.builder_Acar.A_step2 import Astep2


class ABuilderConfig(builder_base.BuilderConfig):
    def __init__(self,staff):
        self.staff = staff


class CreateA(builder_base.Builder):
    def __init__(self,context):
        super().__init__(context)
        self.creat_step()
    def creat_step(self):
        self.add_item(Astep1())
        self.add_item(Astep2())

