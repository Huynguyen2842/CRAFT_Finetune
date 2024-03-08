import torch
import torchvision.models as models

# Dummy model for demonstration purposes
class DummyModel(torch.nn.Module):
    def __init__(self):
        super(DummyModel, self).__init__()
        self.fc = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)

# Create an instance of your model
model = DummyModel()

# Check the availability of GPUs
if torch.cuda.is_available():
    # Get the number of available GPUs
    num_gpus = torch.cuda.device_count()

    # Specify the device_ids based on the number of GPUs
    device_ids = list(range(num_gpus))

    # Use DataParallel to parallelize the model across GPUs
    net = torch.nn.DataParallel(model, device_ids=device_ids).cuda()

    # Print information about the GPUs
    print(f"Using {num_gpus} GPU(s): {device_ids}")
else:
    # If no GPU is available, use the model as is
    net = model

# Dummy input data
dummy_input = torch.randn(16, 10).cuda() if torch.cuda.is_available() else torch.randn(16, 10)

# Forward pass through the model
output = net(dummy_input)
print("Model output shape:", output.shape)

for i in range(torch.cuda.device_count()):
    print(f"GPU {i}: {torch.cuda.get_device_name(i)}")

