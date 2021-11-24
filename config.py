# @author Metro
# @time 2021/10/14
import torch.cuda
import torch.nn.functional as F


class config(object):
    """ Object to hold the config requirements for an agent. """

    def __init__(self):
        self.seed = None
        self.environment = 'FreewheelingIntersection_v0'
        self.requirements_to_solve_game = None
        self.num_episodes_to_run = None
        self.file_to_save_data_results = None
        self.file_to_save_results_graph = None
        self.runs_per_agent = None
        self.visualise_overall_results = None
        self.visualise_individual_results = None
        self.hyperparameters = None
        self.env_parameters = None
        self.use_GPU = None
        self.overwrite_existing_results_file = None
        self.save_model = False
        self.standard_deviation_results = 1.0
        self.randomise_random_seed = True
        self.show_solution_score = False
        self.debug_mode = False

        self.env_parameters = {
            'PHASE_NUM': 8,
            'ACTION_LOW': 5.,
            'ACTION_HIGH': 20.,
            'PAD_LENGTH': 25.,
            'LANE_LENGTH_HIGH': 250.,
            'SPEED_HIGH': 100.,
            'EDGE_IDS': ['north_in', 'east_in', 'south_in', 'west_in'],
            'VEHICLES_TYPES': ['NW_right', 'NS_through', 'NE_left',
                               'EN_right', 'EW_through', 'ES_left',
                               'SE_right', 'SN_through', 'SW_left',
                               'WS_right', 'WE_through', 'WN_left'],
            'YELLOW': 3,
            'LANE_LENGTH': 234.12,
            'SIMULATION_STEPS': 3600,
            'N_STEPS': 5,
            'ALPHA': 0.2,  # TODO
        }

        self.hyperparameters = {
            'device': 'cuda' if torch.cuda.is_available() else 'cpu',
            'epsilon_initial': 1.0,
            'epsilon_final': 0.05,
            'epsilon_decay': 5000,
            'replay_memory_size': 1e6,
            'initial_memory_threshold': 0,
            'batch_size': 64,
            'gamma': 0.99,
            'learning_rate_actor': 1e-4,
            'learning_rate_actor_param': 1e-5,
            'clip_grad': 10,
            'loss_func': F.smooth_l1_loss,
            'tau_actor': 0.01,
            'tau_actor_param': 0.01,
            'hidden_layer_actor': (256, 128, 64),
            'hidden_layer_actor_param': (256, 128, 64),












        }