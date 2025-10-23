from dataclasses import dataclass

@dataclass
class DroneConfig:
    """Configuration parameters for the quadrotor drone."""
    # Physical parameters
    gravity: float = 9.81        # gravitational acceleration in m/s^2
    mass: float = 1.3           # mass of the quadrotor in kg
    
    # Inertia parameters
    inertia_x: float = 0.0153   # mass moment of inertia about x axis in kg*m^2
    inertia_y: float = 0.0153   # mass moment of inertia about y axis in kg*m^2
    inertia_z: float = 0.0307   # mass moment of inertia about z axis in kg*m^2
    
    # Actuator limits
    max_thrust: float = 20.93    # max thrust (N)
    max_torque_rp: float = 2.0   # max roll/pitch torque (N·m)
    max_torque_yaw: float = 1.0  # max yaw torque (N·m)
    
    def __post_init__(self):
        """Validate parameters after initialization."""
        if self.mass <= 0:
            raise ValueError("Mass must be positive")
        if self.max_thrust <= 0:
            raise ValueError("Maximum thrust must be positive")
        if any(i <= 0 for i in [self.inertia_x, self.inertia_y, self.inertia_z]):
            raise ValueError("Inertia values must be positive")

# Create a default configuration instance
config = DroneConfig()