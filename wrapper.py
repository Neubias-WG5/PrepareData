import sys
from subprocess import call

from cytomine.models import Job

from biaflows import CLASS_OBJSEG
from biaflows.helpers import BiaflowsJob, prepare_data


def main(argv):
    # 0. Initialize Cytomine client and job if necessary and parse inputs
    with BiaflowsJob.from_cli(argv) as nj:
        nj.job.update(status=Job.RUNNING, progress=0, statusComment="Initialisation...")

        problem_cls = CLASS_OBJSEG

        # 1. Create working directories on the machine
        # 2. Download the images
        in_images, gt_images, in_path, gt_path, out_path, tmp_path = prepare_data(problem_cls, nj, **nj.flags)

        nj.job.update(status=Job.TERMINATED, progress=100, statusComment="Finished.")


if __name__ == "__main__":
    main(sys.argv[1:])
