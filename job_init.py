from PIPELINE_BASE.PLE_CORE.job import JobsContext
from createcar.Custom import CustomDate
from createcar.builder.builder_Acar.build_Acar import ABuilderConfig
from createcar.carfactory import CarFactory
from createcar.creatjob import Creatcar


custom1 = CustomDate("A",CarFactory())
print(custom1)
with JobsContext(custom1) as job_context:
    A_job = Creatcar(job_context)   #what factory and what type
    builder_config = ABuilderConfig("xiaohong") #which staff
    A_job.run(builder_config)
