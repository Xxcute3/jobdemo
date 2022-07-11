from PIPELINE_BASE.PLE_CORE.job import job_base


class Creatcar(job_base.JobBase):
    name = "CreatCar"
    description = "creat a car"
    def __init__(self,context):
        super().__init__(context)

    def get_real_builder(self):
        '''
        return What kind of Factory
        '''

        factory = self.find_factory()
        if factory is not None:
            return factory.creatCarBuilder(self._job_context)
    def find_factory(self):
        return self._job_context.CustomDate.factory
