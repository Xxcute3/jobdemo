from PIPELINE_BASE.PLE_CORE.job import worker_item

class Astep2(worker_item.WorkerItem):
    name = "step 2"
    description = "A step 2"

    def run_imp(self, context, config):
        context.info("This is the second step in building car A,staff is {}".format(config.staff))
        return True