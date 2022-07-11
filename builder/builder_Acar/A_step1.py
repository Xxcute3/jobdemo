from PIPELINE_BASE.PLE_CORE.job import worker_item


class Astep1(worker_item.WorkerItem):
    name = "step 1"
    description = "A step 1"

    def run_imp(self, context, config):
        context.info("This is the first step in building car A,staff is {}".format(config.staff))
        return True