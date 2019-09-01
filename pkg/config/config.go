package config

import (
	"log"
	"path"

	"github.com/cep21/xdgbasedir"
)

var configDirectoryPath string

type Options struct {
	NoColor         bool
	UpdateBeforeRun bool
	WithTor         bool
	WithTorAddress  string
	WithAdmin       bool
	WithExport      string
	WithFormatAll   bool
	WithHttpCache   bool
	WithFormat      string
	Verbose         bool
	CheckForUpdate  bool
	RequestIP       string
}

// test configor for extra rules
type Config struct {
	APPName string `default:"investigo"`
	DB      struct {
		Name     string
		User     string `default:"root"`
		Password string `required:"true" env:"DBPassword"`
		Port     uint   `default:"3306"`
	}
	Contacts []struct {
		Name  string
		Email string `required:"true"`
	}
	// SiteData []SiteData
}

/*
// WriteConfig writes the configuration information
func (cfg *Config) WriteConfig() error {
	err := os.MkdirAll(configDirectoryPath, 0700)
	if err != nil {
		return err
	}

	data, err := yaml.Marshal(cfg)
	if err != nil {
		return err
	}
	return ioutil.WriteFile(configFilePath(), data, 0600)
}
*/

func init() {
	baseDir, err := xdgbasedir.ConfigHomeDirectory()
	if err != nil {
		log.Fatal("Can't find XDG BaseDirectory")
	} else {
		configDirectoryPath = path.Join(baseDir, ProgramName)
	}
}
