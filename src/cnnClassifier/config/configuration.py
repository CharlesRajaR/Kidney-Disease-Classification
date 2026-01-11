from cnnClassifier.utils.common import create_directories, read_yaml
from cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, TrainingConfig
from cnnClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from pathlib import Path

# print(f"Current working directory : {Path().cwd()}")
# print(f"{CONFIG_FILE_PATH} is exists in the current working directory? => {CONFIG_FILE_PATH.exists()}")
# print(f"{PARAMS_FILE_PATH} is exists in the current working directory? => {PARAMS_FILE_PATH.exists()}")

class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    


    def prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path = Path(config.updated_base_model_path),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate = self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES
        )

        return prepare_base_model_config

    def get_training_config(self) -> TrainingConfig:
        model_training = self.config.model_training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = self.config.data_ingestion.unzip_dir / Path("kidney-ct-scan-image")
        create_directories([model_training.root_dir])

        training_config = TrainingConfig(
            root_dir = model_training.root_dir,
            trained_model_path = Path(model_training.trained_model_path),
            updated_base_model_path = Path(prepare_base_model.updated_base_model_path),
            training_data = training_data,
            params_epochs = params.EPOCHS,
            params_batch_size = params.BATCH_SIZE,
            params_is_augumentation = params.AUGUMENTATION,
            params_image_size = params.IMAGE_SIZE,
            params_learning_rate=params.LEARNING_RATE
        )

        return training_config
